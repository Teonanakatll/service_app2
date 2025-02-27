import { useRef } from "react";
import s from "./MyPosts.module.css";
import Post from "./Post/Post";

const MyPosts = (props) => {


  const postsElements = props.posts.map(el => <Post message={el.message} likesCount={el.likesCount} />)

  const newPostElement = useRef(null)
  
  const addPos  = () => {
    props.dispatch({ type: 'ADD-POST' })
  }

  const onPostChange = () => {
    let text = newPostElement.current.value
    props.dispatch({ type: 'UPDATE-NEW-POST-TEXT', text: text })
  }

  return (
    <div className={s.blockPosts}>
      <h3>My posts</h3>
      <div>
        <div>
          <p>{props.newPostText}</p>
          {/* тут тот принцып useRef - хранение данных между рендерами, что по нашей лгике как раз и вызывает рендер при изменении текущего значения */}
          <textarea onChange={ onPostChange } ref={newPostElement} value={props.newPostText} />
        </div>
        <div>
          {/* Callback функция — это функция, которая передается в другую функцию как аргумент и вызывается
           в определенный момент, например, по завершении какой-либо операции или события. */}
          <button onClick={ addPos } >Add post</button>
        </div>
      </div>
      <div className={`${s.posts}`}>
        New posts
        <br></br>
        {postsElements}
      </div>
    </div>
  );
};
export default MyPosts;
