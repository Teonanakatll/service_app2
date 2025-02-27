import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'

import store from './redux/state.js'
import './index.css'
import App from './App.jsx'


const root = createRoot(document.getElementById('root'));
                              
const rerenderEntireTree = (props) => {
  const state = props.getState()
  root.render(
    // <StrictMode>
    //   <App state={state} addPost={addPost} updateNewPostText={updateNewPostText}
    //   addMessage={addMessage} updateNewMessage={updateNewMessage} />
    // </StrictMode>,
    <StrictMode>
      {/* нельзя передавать метод обьекта отдельно от самого обьекта, так теряется контекст.
      почитать за bind() он возвращает одноимённую функцию в которой передаваемый метод связан с контекстом (своим обьектом) */}
      <App state={state} dispatch={store.dispatch.bind(store)} />
    </StrictMode>
  )  
}
// rerenderEntireTree(state)
rerenderEntireTree(store)

store.subscribe(rerenderEntireTree)