import MyPosts from './MyPosts/MyPosts';
import ProfileInfo from './ProfileInfo/ProfileInfo';


const Profile = (props) => {
  // debugger
  return (
    <div>
      <ProfileInfo />
      <MyPosts posts={props.state.posts}
       dispatch={props.dispatch} />
    </div>
  );
};
export default Profile