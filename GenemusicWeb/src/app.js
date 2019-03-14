import Tone from "tone";
import "@babel/polyfill";
import "./index.css";
import "spectre.css/dist/spectre.min.css";
import Piano from "./piano";
import axios from "axios";

class App {

    constructor(){
        const piano = new Piano(document.getElementById("piano"), { whiteKeys: { width: 30, height: 100 }, blackKeys: { width: 25, height: 50 }, numKeys: 7 });
        piano.draw();
        this.piano = piano;
        this.setEvents();
    }

    setEvents = () => {
        document.querySelector("button").addEventListener("click", this.startTone);
    }

    startTone = async () => {
        Tone.Transport.start();
        
        this.specie = await this.evolve();
        this.notes = this.specie.result[299].map((individual) => individual.note);
        var synth = new Tone.Synth().toMaster();
        
        var seq = new Tone.Sequence((time, note) => {
            
            synth.triggerAttackRelease(note, "2n", time);
            
            this.piano.setNote(note.replace(/[0-9]/, ""), true);
            
            this.piano.draw();
            
            this.piano.setNote(note.replace(/[0-9]/, ""), false);
            //straight quater notes
        }, this.notes, "4n");
        
        seq.loop = false;
        seq.start();
    }

    evolve = async () => {
        const res = (await axios.get("http://localhost:3000/run?pop=300&max_gen=300&scale=CMAJ")).data;
        return res
    }
}

new App();