$(() => {
    $("#add-nav-item").click(() => {
        let templateHtml = $("#row-template").html().toString();
        getNextItemId((data) => {
            let newId = data;

            templateHtml = templateHtml.split("#itemid#").join(newId);
            templateHtml = "<tr id='item-id-" + newId + "'>" + templateHtml + "</tr>";
            $("#nav-table-body").append(templateHtml);

            $("#nav-item-save-" + newId).click(handleButtonClicks);
            $("#nav-item-remove-" + newId).click(handleButtonClicks);
            $("#nav-item-title-" + newId).change(handleTextChanges);
            $("#nav-item-link-" + newId).change(handleTextChanges);
        });

        addEmptyItem();
    });

    $("button").click(handleButtonClicks);
    $("input[type='text']").change(handleTextChanges);
});

let getNextItemId = (callback) => {
    $.ajax("/cms-admin/api/get-next-nav-item-id", {
        success: (data, status, xhr) => {
            callback(data);
        }
    })
};

let addEmptyItem = () => {
    $.ajax("/cms-admin/api/add-empty-nav-item", {});
};

let editItem = (itemid, title, link) => {
    $.post("/cms-admin/api/edit-nav-item/" + itemid,
        {'link': link, 'title': title}, (data, status, xhr) => {});
};

let deleteItem = (itemid) => {
    $.ajax("/cms-admin/api/delete-nav-item/" + itemid, {});
};

let handleTextChanges = (event) => {
    let splitId = event.target.id.split("-");
    let id = splitId[splitId.length - 1];

    console.log(id);

    $("#nav-item-save-" + id).prop("disabled", false);
};

let handleButtonClicks = (event) => {
    if (event.target.id == "add-nav-item")
        return;

    let splitId = event.target.id.split("-");
    let id = splitId[splitId.length - 1];
    console.log(id);
    if (event.target.id.toString().indexOf("remove") > -1) {
        // remove button has been pressed
        deleteItem(id);
        $("#item-id-" + id).remove();
    } else {
        // save button has been pressed
        let itemTitle = $("#nav-item-title-" + id).val();
        let itemLink = $("#nav-item-link-" + id).val();

        $("#nav-item-save-" + id).prop("disabled", true);
        editItem(id, itemTitle, itemLink);
    }
};