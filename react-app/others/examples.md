# sdfsdfasf
- sdfsdf 
*sdfsdf*  _sfsdf_
* sdfsdf [http://sdfsdf.com]
![текст изображения](url)

_                                                 __map()__

> map - это свойство массива которое всегда принимает стрелочную функцию (как и forEach/reduce)
```js
const newArray = oldArray.map((el) => {
	return isMaleName(el) ? 1 : 0;
})
```

***                                                      filter()**
```jsx
const onlineList = props.state.dialogsPage.dialogs.filter(dialog => dialog.online)
const onlineList = props.state.dialogsPage.dialogs.filter(dialog => dialog.online === true)
```

***                                                        push()**
> добавляет в конец массива новый элемент
```jsx
posts.push(newPost)
```


> если стрелочная функция имеет условие в 1 строку то можно воспользоваться неявным возвратом
```js
const newArray = oldArray.map((name) => isMaleName(name) ? : 0)
const newArray = oldArray.map(name => `<li> ${name} </li>`)
const newArray = oldArray.map(phrase => {
	return {
		eng: phrase,
		ru: translateRu(phrase)
	}
})
```
> если неявно вернуть нужно обьект то оборачиваем обьект в круглые скобки потому что 
> фигурные в стрелочной функции после стрелки означают тело функции
```js
const newArray = oldArray.map(phrase => ({eng: phrase, ru: translateRu(phrase)}))
```

***                                        структура проекта**
```js
                                            <App />

                                       <BrowserRouter />

                   <Routes />                      								<Navbar />   <Header />

    <Route path="/profile" element={<Profile />} />  or  ...
```
![текст изображения](../../../screens/Screenshot_1.png)

> road map для начала, необходимо знать
![текст изображения](../../../screens/Screenshot_2.png)


> копирует содержимое profilePage, тоесть копирует ссылку на содержание его обьекта и в 
> обьекте который принимает этот пропс при обращении к state будет доступ к его полям
```js
<Route path="/profile" element={<Profile state={props.state.profilePage} />} />
```


***                                                 callback функция**

> Callback функция — это функция, которая передается в другую функцию как аргумент и вызывается
>	в определенный момент, например, по завершении какой-либо операции или события.
<button onClick={ addPost } >Add post</button>