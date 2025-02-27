import s from '../Navbar.module.css'
import DialogItem from '../../Dialogs/DialogItem/DialogItem'

const OnlineList = ({onlineList, onlineSection}) => {

	const list = onlineList.map(el => <DialogItem id={el.id} name={el.name} ava={el.ava} online={el.online} onlineSection={onlineSection} />)

	return (
		<div className={s.onlineBox}>
			<span>Online:</span> 
		<div className={s.onlineWrap} >
			{list}
		</div>
		</div>
	)
}
export default OnlineList