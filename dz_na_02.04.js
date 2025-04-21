class Rectangle {
    constructor(topLeftX, topLeftY, bottomRightX, bottomRightY) {
      this.topLeft = { x: topLeftX, y: topLeftY };
      this.bottomRight = { x: bottomRightX, y: bottomRightY };
    }
  
    printInfo() {
      console.log(`Прямоугольник с координатами:
      Левая верхняя точка: (${this.topLeft.x}, ${this.topLeft.y})
      Правая нижняя точка: (${this.bottomRight.x}, ${this.bottomRight.y})`);
    }
  
    get width() {
      return Math.abs(this.bottomRight.x - this.topLeft.x);
    }
  
    get height() {
      return Math.abs(this.topLeft.y - this.bottomRight.y);
    }
  
    get area() {
      return this.width * this.height;
    }
  
    get perimeter() {
      return 2 * (this.width + this.height);
    }
  
    changeWidth(delta) {
      this.bottomRight.x += delta;
    }
  
    changeHeight(delta) {
      this.bottomRight.y += delta;
    }
  
    changeDimensions(widthDelta, heightDelta) {
      this.changeWidth(widthDelta);
      this.changeHeight(heightDelta);
    }
  
    moveX(delta) {
      this.topLeft.x += delta;
      this.bottomRight.x += delta;
    }
  
    moveY(delta) {
      this.topLeft.y += delta;
      this.bottomRight.y += delta;
    }
  
    move(xDelta, yDelta) {
      this.moveX(xDelta);
      this.moveY(yDelta);
    }
  
    isPointInside(pointX, pointY) {
      const minX = Math.min(this.topLeft.x, this.bottomRight.x);
      const maxX = Math.max(this.topLeft.x, this.bottomRight.x);
      const minY = Math.min(this.topLeft.y, this.bottomRight.y);
      const maxY = Math.max(this.topLeft.y, this.bottomRight.y);
      
      return pointX >= minX && pointX <= maxX && 
             pointY >= minY && pointY <= maxY;
    }
  }
  
  const rect = new Rectangle(10, 20, 30, 10);
  rect.printInfo();
  console.log("Ширина:", rect.width);
  console.log("Площадь:", rect.area);
  rect.move(5, -3);
  rect.printInfo();
  console.log("Точка (12,15) внутри?", rect.isPointInside(12, 15));