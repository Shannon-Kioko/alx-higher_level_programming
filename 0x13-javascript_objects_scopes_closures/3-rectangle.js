#!/usr/bin/node
class Rectangle {
    width;
    height;
    constructor(w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }

    print() {
        for (let r = 0; r < this.height; r++) {
            let Recty = ''
            for (let c = 0; c < this.width; c++) {
                Recty += "X"
            }
                console.log(Recty);
        }
    }
}
module.exports = class Rectangle { }

const r1 = new Rectangle(3, 8)
r1.print()
