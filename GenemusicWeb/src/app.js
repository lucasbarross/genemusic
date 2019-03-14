import Tone from "tone";
import "./index.css";
import "spectre.css/dist/spectre.min.css";
import Piano from "./piano";

new Piano(document.getElementById("piano"), { whiteKeys: { width: 30, height: 100 }, blackKeys: { width: 25, height: 50 }, numKeys: 7 }).draw()

//play a middle 'C' for the duration of an 8th note
document.querySelector("button").addEventListener("click", (evt) => {
    Tone.Transport.start();
    
    var synth = new Tone.Synth().toMaster();

    var seq = new Tone.Sequence(function(time, note){
        synth.triggerAttackRelease(note, "2n", time);
    //straight quater notes
    }, ["E4", "E4", "F4", "G4", "G4", "F4", "E4", "D4", "C4", "C4"], "4n");

    seq.loop = false;
    seq.start()
});