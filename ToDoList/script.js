// Global counter
let counter = 0 

// Global variables
let currentItemId = null;

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

const renamedItem = document.getElementById("renameInput");

// This is a collection because there are multiple
const allLabelContainers = document.getElementsByClassName("container");

// This is a collection because there are multiple
const optionsMenuButtons = document.getElementsByClassName("options");

const optionButtons = document.getElementsByClassName("optionBtn");
const optionsMenuContainer = document.getElementsByClassName("optionsContainer");

// Options Menu Buttons
const renameButton = document.getElementById("renameButton");
const deleteButton = document.getElementById("deleteButton");

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
    renamedItem.value = "";
}

function optionsOverlayClose(){
    const optionsOverlay = document.getElementsByClassName("optionsOverlay");
    for (const overlay of optionsOverlay){
        overlay.style.opacity = "0";
    };
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
    newItemMenuButton.id = "item-" + counter;
    const newItemButtonLink = document.createElement("a");
    newItemButtonLink.href = "#OptionsToDo";

    // Get parent container
    const listContainer = document.getElementById("toDoListContainer");

    // Add label to parent container
    listContainer.appendChild(newItemLabel);

    // Add elements to label
    newItemLabel.appendChild(newItemInput);
    newItemLabel.appendChild(newItemSpan);
    newItemLabel.appendChild(newItemButtonLink);

    // Get and add textbox value to label
    const newItemValue = document.createTextNode(itemValue);
    newItemLabel.appendChild(newItemValue);

    // Add button to anchor element
    newItemButtonLink.appendChild(newItemMenuButton);

    // Create values for buttons and add to them
    const buttonValue = document.createTextNode("⁝");
    newItemMenuButton.appendChild(buttonValue);

    // Increment counter
    counter ++;

    // Loop through each options button and add an event listener
    for (const menuButton of optionsMenuButtons){
        console.log(menuButton);
        menuButton.addEventListener("click", retrieveElementId);
    };

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

function retrieveElementId(event) {
    const clickedElement = event.target;
    const buttonId = clickedElement.getAttribute('id');
    currentItemId = buttonId;
    console.log(currentItemId);
}

function renameItem(){
    const newName = renamedItem.value;
    const itemToRename = document.getElementById(currentItemId);
    const parentContainer = itemToRename.parentElement;
    const grandparentContainer = parentContainer.parentElement;
    for (const child of grandparentContainer.childNodes){
        if (child.nodeType === Node.TEXT_NODE){
            child.nodeValue = newName;
            console.log(child.nodeValue);
        };
    };
    // Reset textbox
    resetTextBoxValue();

    // Change overlay opacity
    optionsOverlayClose();
}

function deleteItem(){
    // Access item by global variable 
    const itemToDelete = document.getElementById(currentItemId);

    // Track back to grandparent container
    const parentContainer = itemToDelete.parentElement;
    const grandparentContainer = parentContainer.parentElement;

    // Remove container
    grandparentContainer.remove();

    // Change overlay opacity
    optionsOverlayClose();
}

addButton.addEventListener("click", addListItems);
newItem.addEventListener("keypress", addListItems);
renameButton.addEventListener("click", renameItem);
deleteButton.addEventListener("click", deleteItem);


// const itemToRename = document.getElementById(currentItemId);
// const parentContainer = itemToRename.parentElement;
// const grandparentContainer = parentContainer.parentElement;
// console.log(grandparentContainer);
// for (const child of grandparentContainer.childNodes){
//     if (child.nodeType === Node.TEXT_NODE){
//         const containerText = child.nodeValue;            
//         console.log(containerText);
//         return containerText;
//     };
// };

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