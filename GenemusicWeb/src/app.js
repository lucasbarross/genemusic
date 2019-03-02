import Tone from "tone";
import "./index.css";
//create a synth and connect it to the master output (your speakers)

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