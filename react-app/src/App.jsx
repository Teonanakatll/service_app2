import Header from "./components/Header/Header";
import Navbar from "./components/Navbar/Navbar";
import Profile from "./components/Profile/Profile";
import Dialogs from "./components/Dialogs/Dialogs";
import News from "./components/News/News";
import Music from "./components/Music/Music";
import Settings from "./components/Settings/Settings";

// npm react-router-dom
import { Routes, Route, BrowserRouter } from "react-router-dom";
import "./App.css";

const App = (props) => {
  // debugger
  const onlineList = props.state.dialogsPage.dialogs.filter(dialog => dialog.online)

  return (
    <BrowserRouter>
      <div className="app-wrapper">
        <Header />
        <Navbar onlineList={onlineList} />
        <div className={`app-wrapper-content gitem`}>
          <Routes>
            {/* копирует содержимое profilePage, тоесть копирует ссылку на содержание его обьекта и в 
            обьекте который принимает этот пропс при обращении к state будет доступ к его полям.
            РОУТИНГ НИОТЧЕГО НЕ ЗАВИСИТ ЕГО ЗАДАЧА СЛЕДИТЬ ЗА АДРЕСНОЙ СТРОКОЙ!! */}
            <Route path="/profile" element={<Profile state={props.state.profilePage} dispatch={props.dispatch} />} />
            <Route path="/dialogs/*" element={<Dialogs state={props.state.dialogsPage} dispatch={props.dispatch} />} />
            <Route path="/news" element={<News />} />
            <Route path="/music" element={<Music />} />
            <Route path="/settings" element={<Settings />} />
          </Routes>
        </div>

      </div>
    </BrowserRouter>
  );
};

export default App;
