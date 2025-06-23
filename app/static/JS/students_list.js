document.addEventListener('DOMContentLoaded', async function () {
    const studentsList = document.getElementById('items-list');

    // Telegram WebApp integration
    // const initData = window.Telegram?.WebApp?.initData || '';
    const initData = 'query_id=AAFg9PcZAAAAAGD09xmIlYWB&user=%7B%22id%22%3A435680352%2C%22first_name%22%3A%22%D0%A8%D1%83%D1%80%D0%B0%22%2C%22last_name%22%3A%22%F0%9F%AB%A7%22%2C%22username%22%3A%22tiswy%22%2C%22language_code%22%3A%22ru%22%2C%22allows_write_to_pm%22%3Atrue%2C%22photo_url%22%3A%22https%3A%5C%2F%5C%2Ft.me%5C%2Fi%5C%2Fuserpic%5C%2F320%5C%2FLTSz7fDSMDMNKVRn5rp3I7AwoBuEu6bL3jqMwWX_Oko.svg%22%7D&auth_date=1749603174&signature=jhQa1Xq-7CcZOBTrCog8HAG_uJL6ySlCU7O3LZcuk3RU8Bl3CNEvNdP0D_ZhmySwpf3wqnOd7bQKjYfyV3iqAA&hash=2b69ff38d9d7230eebc12ca33f56e5c8b70d97372f01af1eb016580a39e42dd4';

    loadStudents();

    async function loadStudents() {
        try {
            const response = await fetch('/api/students', {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${initData}`
                }
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            if (response.status === 204) {
                studentsList.innerHTML = '<div>Пока студентов нет!</div>';
                return;
            }

            const data = await response.json();
            if (data.status === 'success') {
                studentsList.innerHTML = '';
                const students = JSON.parse(data.data);
                students.forEach(student => {
                    const userId = student.user_id;
                    const fullName = `${student.first_name || ''} ${student.last_name || ''}`.trim();
                    const subject = student.subject_info || 'No subject';
                    studentsList.appendChild(createItem(fullName, subject, openProfile(userId)));
                });
            } else {
                console.error('API error:', data.message);
            }
        } catch (error) {
            console.error('Failed to load students:', error);
        }
    }

    function openProfile(userId) {
        return function() {
            window.location.href = `/profile?user_id=${userId}`;
        };
    }
});