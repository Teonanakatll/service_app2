import s from "./ProfileInfo.module.css";

const ProfileInfo = () => {
  return (
    <div>
      <img
        className={s.imgProfile}
        src="https://cdn.tripster.ru/thumbs2/2a9a60e0-fcdb-11ed-bb0b-a25e06629b62.1220x600.jpeg"
        alt=""
      />
    </div>
  );
};
export default ProfileInfo;
