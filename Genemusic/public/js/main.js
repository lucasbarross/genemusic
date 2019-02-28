document.querySelector('button').addEventListener('click', () => Tone.start())

var synth = new Tone.Synth().toMaster();

synth.triggerAttackRelease("C4", "8n");