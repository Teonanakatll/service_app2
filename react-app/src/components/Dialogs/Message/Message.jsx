import { NavLink } from "react-router-dom";
import s from "./../Dialogs.module.css";


const Message = (props) => {
  return <div className={props.my ? `${s.message} ${s.my_message}` : s.message}>{props.message}</div>
  
};

export default Message;
