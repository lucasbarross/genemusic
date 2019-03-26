//@ts-check
import Tone from "tone";
import "./index.css";
import "spectre.css/dist/spectre.min.css";
import Piano from "./piano";
import History from "./history";
import axios from "axios";
import "@babel/polyfill";

class App {

    constructor(piano){
        this.history = new History();
        this.piano = piano;
        this.piano.draw();
        this.setEvents();
    }

    setEvents = () => {
        document.getElementById("evolve-btn").addEventListener("click", this.evolve);
    }

    startTone = async () => {
        Tone.Transport.start();
        
        // this.specie = await this.evolve();
        // this.notes = this.specie.result[299].map((individual) => individual.note);
        var synth = new Tone.Synth().toMaster();
        
        var seq = new Tone.Sequence((time, note) => {
            
            synth.triggerAttackRelease(note, "2n", time);
            
            this.piano.setNote(note.replace(/[0-9]/, ""), true);
            
            this.piano.draw();
            
            this.piano.setNote(note.replace(/[0-9]/, ""), false);
            //straight quater notes
        }, ["C5", "D4", "A2"], "4n");
        
        seq.loop = false;
        seq.start();
    }

    evolve = async () => {
        try {
            const generations = (await axios.get("http://localhost:3000/run?pop=300&max_gen=300&scale=CMAJ")).data;
            this.history.updateGenerationsBar(generations);
        } catch (err) {
            console.log(err);
        }
    }
}

const piano = new Piano(document.getElementById("piano"), 
    { 
        whiteKeys: { width: 30, height: 100 }, 
        blackKeys: { width: 25, height: 50 }, 
        numKeys: 7 
    });


new App(piano);