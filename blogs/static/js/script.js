window.addEventListener('DOMContentLoaded', function() { // все функции/события/методы прописаны внутри этой функции, она проходит по всему DOM при загрузке скрипта и ищет нужные элементы
    var nodes = document.querySelectorAll('.header-menu .hamburger');// ищу элемент в DOM
    var text = document.querySelectorAll('.box .description p');// ищу элемент в DOM
    var btn = document.querySelectorAll('.subscription-form form .submit .btn');// ищу элемент в DOM
    [].forEach.call(nodes, function(a) { // прохожу по DOM и ищу элемент в переменной "nodes"
        a.addEventListener('click', function() { // создаю событие на 'click' по найденной кнопке
            [].forEach.call(document.querySelectorAll('.header-menu'), function (d) { // при нажатии навешиваю класс "open" на требуемый элемент
                d.classList.toggle("open")
        });
      });
    });
    [].forEach.call(text, function (s) { //функция с передающемся аргументом
        var size, obj;
        obj = s.innerHTML; //
        size = 100;
        if (obj.length > size){ // считаем длинну строки (если длинна строки больше 100 символов)
            obj = obj.slice(0,100);// обрезаем до 100 символов
        }
        s.innerHTML = obj + '...';// вставляем в DOM обрезанный текст и троеточие в конце
    });
       [].forEach.call(btn, function (e) {
            e.addEventListener('click', function (th) {
                var name = document.getElementById('name-sb').value; //Получение с формы поля "Имя"
                var surname = document.getElementById('surname-sb').value; //Получение с формы поля "Фамилия"
                var email = document.getElementById('email-sb').value; //Получение с формы поля "Почта"
                th.preventDefault(); //отменить действие кнопки по умолчанию
                if (name != 0 && surname != 0 && email != 0) {
                    [].forEach.call(document.querySelectorAll('#modalwindow'), function (g) {// при нажатии навешиваю класс "opened" на требуемый элемент
                        g.classList.add("opened");
                    }); // навесить класс "Open" на модальное окно
                    var complete = document.getElementById ('description');
                    var object = document.createElement('div');// создаём пустой Div в DOM
                    object.innerHTML = '<div id="subscribe">'+ // Делаем структуру и ложим значение с нужный полей
                                           '<div class="first-name">'+name +'</div>'+
                                           '<div class="last-name">'+ surname +'</div>'+
                                        '</div>';
                    complete.appendChild(object);// добавляем структуру в DOM
                }
            });
        });
        var close = document.querySelectorAll('#btn-close');
        [].forEach.call(close, function (x) { // при клике закрываем POPUP
            x.addEventListener('click',function () {
                [].forEach.call(document.querySelectorAll('#modalwindow'), function (cl) {
                    cl.classList.remove("opened");// удаляем класс opened
                    var desc = document.getElementById('subscribe');
                    if (desc != null){
                        desc.parentNode.remove(desc);// удаляем структуру со значениями
                    }
                });
            });
        });
    /**Страница регистрации **/
    db = openDatabase("Corgi_DB", "0.1", "A list of to do items.", 200000); // открываем базу данных, если её нет, то создаём
    db.transaction(function(tx) {
            tx.executeSql("CREATE TABLE User (Name REAL UNIQUE, Surname TEXT, Email TEXT, Password VARCHAR, Rpassword VARCHAR)", [], null, null); // создаём таблицу Пользователей
    });
    var btn_reg = document.querySelectorAll('.register-page .btn-reg');
    [].forEach.call(btn_reg, function (sub) {
        sub.addEventListener('click', function (click) {
            var name = document.getElementById('name').value; //Получение с формы поля "Имя"
            var surname = document.getElementById('surname').value; //Получение с формы поля "Фамилия"
            var email = document.getElementById('email').value; //Получение с формы поля "Почта"
            var password = document.getElementById('password').value; //Получение с формы поля "Почта"
            var r_password = document.getElementById('r-password').value; //Получение с формы поля "Почта"
            click.preventDefault();// отменяем действие кнпоки по умолчанию
            if (r_password.length == 0 || password.length == 0 || email.length == 0){ // проверяем поле, на пустоту
                alert('Заполните обязательные поля');
            } else if (password != r_password){ // проверяем 2 поля "Пароль" и "Повторите пароль", чтобы пароли совпадали
                alert('Пароли не совпадают');
            } else  {
                db.transaction(function(tx) {
                    tx.executeSql("INSERT INTO User (Name, Surname, Email, Password, Rpassword) values(?, ?, ?, ?, ?)", [name, surname, email, password, r_password], null, null); // записываем в БД полученные значения
                });
            }
        })
    });
    var btn_login = document.querySelectorAll('#btn-login');
    [].forEach.call(btn_login,function (l) {
       l.addEventListener('click', function (login) {
          var email = document.getElementById('email-log').value;
          var password = document.getElementById('password-log').value;
          login.preventDefault(); // отменяем действие кнпоки по умолчанию
           db.transaction(function(tx) {
               tx.executeSql("SELECT * FROM User", [], function(tx, result) {
                   for(var i = 0; i < result.rows.length; i++) { // достаём из БД поля для регистрации
                       var bd_em = result.rows.item(i)['Email'];
                       var bd_pass = result.rows.item(i)['Password'];
                       var bd_name = result.rows.item(i)['Name'];
                   }
                   if (bd_em != email || bd_pass != password) { //проверка на существование в БД эмейла и пароля, введённых пользователем
                       alert('Неправильный логин или пароль');
                   } else {
                       window.location.href = 'homepage_reg.html'; //если эмейл и пароль были введены корректно перенаправляем на страницу для зарегестрированных пользователей
                       alert('Добро Пожаловать ' + bd_name);
                   }
                   }, null)});
       });
    });
});
