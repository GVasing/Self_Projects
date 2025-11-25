// Get elements
const firstRightArrow = document.getElementById("homerightarrow");
const secondRightArrow = document.getElementById("toDoRightArrow");
const thirdRightArrow = document.getElementById("inProgressRightArrow");

const firstLeftArrow = document.getElementById("toDoLeftArrow");
const secondLeftArrow = document.getElementById("inProgressLeftArrow");
const thirdLeftArrow = document.getElementById("completeLeftArrow");

const home = document.getElementById("home");
const toDo = document.getElementById("todo");
const inProgress = document.getElementById("inprogress");
const completed = document.getElementById("completed");

const addButton = document.getElementById("addBtn");
const newItem = document.getElementById("toDoItem");

const allListContainers = document.getElementsByClassName("list_container");

const optionsMenuButton = document.getElementsByClassName("options");
const optionButtons = document.getElementsByClassName("optionBtn");
const optionsMenuContainer = document.getElementsByClassName("optionsContainer");

function changePage(element, section){
    element.addEventListener("click", function(){
        section.scrollIntoView({behavior: "smooth", inline: "center"});
    })
}

changePage(firstRightArrow, toDo);
changePage(firstLeftArrow, home);
changePage(secondRightArrow, inProgress);
changePage(secondLeftArrow, toDo);
changePage(thirdRightArrow, completed);
changePage(thirdLeftArrow, inProgress);

function resetTextBoxValue(){
    newItem.value = "";
}

function createNewListItem(){
    // Get text value
    const itemValue = newItem.value;

    // Create elements and attributes required
    const newItemLabel = document.createElement("label");
    newItemLabel.className = "container";
    const newItemInput = document.createElement("input");
    newItemInput.type = "checkbox";
    const newItemSpan = document.createElement("span");
    newItemSpan.className = "checkmark";
    const newItemMenuButton = document.createElement("button");
    newItemMenuButton.className = "options";
    const newItemMenuContainer = document.createElement("div");
    newItemMenuContainer.className = "optionsContainer";
    const deleteButton = document.createElement("button");
    const renameButton = document.createElement("button");
    deleteButton.className = "optionBtn";
    renameButton.className = "optionBtn";

    // Get parent container
    const listContainer = document.getElementById("toDoListContainer");

    // Add label to parent container
    listContainer.appendChild(newItemLabel);

    // Add elements to label
    newItemLabel.appendChild(newItemInput);
    newItemLabel.appendChild(newItemSpan);
    newItemLabel.appendChild(newItemMenuButton);
    newItemLabel.appendChild(newItemMenuContainer);
    newItemMenuContainer.appendChild(deleteButton);
    newItemMenuContainer.appendChild(renameButton);

    // Get and add textbox value to label
    const newItemValue = document.createTextNode(itemValue);
    newItemLabel.appendChild(newItemValue);

    // Create values for buttons and add to them
    const buttonValue = document.createTextNode("⁝");
    const deleteBtnValue = document.createTextNode("Delete");
    const renameBtnValue = document.createTextNode("Re-Name");
    newItemMenuButton.appendChild(buttonValue);
    deleteButton.appendChild(deleteBtnValue);
    renameButton.appendChild(renameBtnValue);

    // Reset textbox
    resetTextBoxValue();
}

function addListItems(event){
    if (event.type === "click"){
        createNewListItem();
    } else if (event.type === "keypress"){
        if (event.key === "Enter"){
            createNewListItem();
        }
    }
}

addButton.addEventListener("click", addListItems);
newItem.addEventListener("keypress", addListItems);

// optionsMenuButton.addEventListener("click", function(){
//     const optionsMenuOverlay = document.getElementsByClassName("optionsOverlay");
//     optionsMenuOverlay.style.opacity = "1";
// })

// optionsMenuButton.addEventListener("click", function(){
//     const optionMenuContainer = document.getElementsByClassName("optionsContainer");
//     optionMenuContainer.style.display = ""
// })

// const sections = {
//     0: home,
//     1: toDo,
//     2: inProgress
// };

// // const leftArrows = document.getElementsByClassName("leftarrow")
// const leftArrows = document.querySelectorAll(".leftarrow");
// const rightArrow = document.getElementsByClassName("rightarrow")

// function goBackwards(sectionId){
//     leftArrows.forEach(item => {
//         item.addEventListener("click", function(){
//             const desiredSect = document.getElementById(`${sectionId}`);
//             desiredSect.scrollIntoView({behavior: "smooth", inline: "center"});
//         });
//     })
// }

// goBackwards("home");