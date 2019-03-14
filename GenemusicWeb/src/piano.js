class Piano { 

    constructor(canvas, config) {
        this.canvas = canvas;
        this.config = config;
        this.canvas.width = this.config.numKeys * this.config.whiteKeys.width + 2;
        this.canvas.height = this.config.whiteKeys.height + 60;
        this.context = canvas.getContext("2d");
        this.keyStates = [];
    }

    draw() {
        const midheight = (this.canvas.height - this.config.whiteKeys.height)/2;
        this.drawWhiteKeys(midheight);
        this.drawBlackKeys(midheight);
    }
    
    drawWhiteKeys(midheight) {
        for(let i = 0; i < this.config.numKeys; i++) {
            this.context.rect(30 * i + 1, midheight, this.config.whiteKeys.width, this.config.whiteKeys.height);   
        }
        this.context.stroke();
    }
    
    drawBlackKeys(midheight) {
        this.context.beginPath();
        
        for(let i = 0; i < 2; i++) {
            this.context.rect((31 + 31 * i) - this.config.blackKeys.width/2, midheight, this.config.blackKeys.width, this.config.blackKeys.height);
        }
        
        for(let i = 0; i < 3; i++) {
            this.context.rect((121 + 31 * i) - this.config.blackKeys.width/2, midheight, this.config.blackKeys.width, this.config.blackKeys.height);
        }

        this.context.fill();
    }
    
}

module.exports = Piano;