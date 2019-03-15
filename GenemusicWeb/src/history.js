//@ts-check

import generationsBar from "./components/generationsBar";

export default class History {

    constructor() {
        this.generations = null;
    }

    updateGenerationsBar(generations) {
        const parent = document.getElementById("generations-bar");

        for(let i = 0; i < generations.result.length; i++) {

            const content = document.createTextNode(generationsBar(i));

            parent.appendChild(content);
        }
    }
}