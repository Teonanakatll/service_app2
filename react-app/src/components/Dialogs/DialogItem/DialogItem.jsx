import { NavLink } from "react-router-dom";
import s from "./../Dialogs.module.css";

const DialogItem = ({id, name, online, ava, ...props}) => {
  // debugger
  
  let path = `/dialogs/${id}`;
  return (
    <div className={props.onlineSection ? `${s.dialog} ${s.onlineSection}` : s.dialog}>
      
      <NavLink className={({isActive}) => isActive ? s.active : s.link} to={path}>
        {name}
        <img className={s.ava} src={ava} alt="" />
      </NavLink>
      <div className={online ? `${s.ind} ${s.online}` : s.ind} ></div>
    </div>
  );
};

export default DialogItem;
