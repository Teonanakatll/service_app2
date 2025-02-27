import s from "./TextArea.module.css";
import { useRef } from "react";

const TextArea = ({onClick}) => {

	const newPostElement = useRef(null)

	const text = newPostElement.current.value

  return (
    <div>
      <div>
        <textarea ref={newPostElement}></textarea>
      </div>
      <div>
        {/* Callback функция — это функция, которая передается в другую функцию как аргумент и вызывается
							 в определенный момент, например, по завершении какой-либо операции или события. */}
        <button onClick={onClick}>Add post</button>
      </div>
    </div>
  );
};
export default TextArea
