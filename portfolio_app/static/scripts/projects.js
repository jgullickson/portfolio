function selectTab(tabIndex) {

    let tabs = document.getElementsByClassName("tab");
    
    for (const tab of tabs) {
        if (tab.id === `tab-${tabIndex}`) {
            tab.classList.add('is-active');
        } else {
            tab.classList.remove('is-active');
        }
    }

    let tabLinks = document.getElementsByClassName("tab-link");

    for (const tabLink of tabLinks) {
        if (tabLink.id === `tab-link-${tabIndex}`) {
            tabLink.classList.add('is-active');
        } else {
            tabLink.classList.remove('is-active')
        }
    }
}