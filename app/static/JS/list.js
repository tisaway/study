function createItem(title, description, itemFunction) {
    const item = document.createElement('div');
    item.className = 'item';
    item.innerHTML = `
        <div>
            <div class="item-title">${title}</div>
            <div class="item-description">${description}</div>
        </div>
        <div class="go-arrow"></div>
    `;
    item.addEventListener('click', itemFunction);
    return item;
}