const displayDeleteConfigmationDialog = (itemName) => {
    return confirm("Do you really want to delete item '" + itemName + "'");
};

window.addEventListener("load", (event) => {
    let editLinkTags = document.querySelectorAll("a");
    for (let i = 0; i < editLinkTags.length; i++) {
        let tag = editLinkTags[i];

        if (tag.innerHTML === "Remove")
            tag.addEventListener("click", (event) => {
                event.preventDefault();

                let itemName = event.target.parentNode.parentNode.querySelector("td").innerHTML;
                if(displayDeleteConfigmationDialog(itemName))
                    window.location = event.target.getAttribute("href")
            })
    }
});