import s from "./Post.module.css";

const Post = (props) => {
  return (
    <div className={`${s.item}`}>

      <img
      src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFUrnudOvc7-M9syb6Cx6g3BAa4tGLIjezMQ&s"
        alt=""
      />
      {props.message} likes: {props.likesCount}
      <div><span>Like</span></div>
    </div>
  );
};
export default Post;
