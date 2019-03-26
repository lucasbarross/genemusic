//@ts-check

import generationsBar from "./components/generationsBar";

export default class History {

    constructor() {
        this.generations = null;
    }

    updateGenerationsBar(generations) {
        const parent = document.getElementById("generations-bar");
        
        for(let c = 0; c < parent.children.length; c++) {
            parent.children[c].remove();
        }

        for(let i = 0; i < generations.result.length; i++) {
            
            const newDiv = document.createElement("div");
            
            newDiv.setAttribute("data-id", `${i}`);
            newDiv.setAttribute("class", "generation");

            parent.appendChild(newDiv);
        }
    }
}