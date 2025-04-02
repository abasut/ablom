//Создание классов и объектов
class Rectangle{
    X1Y1;
    X2Y2;
    constructor(X1Y1, X2Y2){
        this.X1Y1 = X1Y1;
        this.X2Y2 = X2Y2
    }
    print(){//Функция вывода 
        return
        ( $(this.X1Y1[0]),  $(this.X1Y1[1]) ), 
        ( $(this.X2Y2[0]),  $(this.X2Y2[1]) ) ;
    }
    //Функция ширины
    widthRect(){
        this.width = this.X2Y2[0] - this. X1Y1[0];
        console.log("Данные по высоте подсчитаны");
    }
    //Функция высоты
    heightRect(){
        this.heigth = this.X2Y2[1] - this.X1Y1[1]
        console.log("Данные по высоте подсчитаны!")
            }
    //Функция площади
    s(){//Проверка 0 значения для ширины и высоты
        if (this.heigth == 0) or (this.width == 0)(
            this.widthRect();
            this.heightRect();
            )
            return 'F = $(this.height + this.width)'
     }
    //Функция периметра 
    //Функция SET ширины
    //Функция GET ширины
    //Функция SET высоты 
    //Функция GET высоты 
    //Функция Изменения высоты и ширины 
    //Функция смещения по оси X 
    //Функция смещения по оси Y
    //Функция смещения по оси X и Y 
    //Функция для проверки нахождения внутри RECTANG1E 
 }
X1 = +prompt("Введите координату X1:")
Y1 = +prompt("Введите координату Y1:")
X2 = +prompt("Введите координату X2:")
Y2 = +prompt("Введите координату Y2:")
