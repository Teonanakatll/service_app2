// let rerenderEntireTree = () => {
//   console.log('State was changed');
// }

// const state = {
//   profilePage: {
//     posts: [
//       { di: 1, message: "Hi, how are you?", likesCount: 11 },
//       { di: 1, message: "It's my first post", likesCount: 12 },
//       { di: 1, message: "What is it man?", likesCount: 5 },
//       { di: 1, message: "I'm ready up and runing!", likesCount: 100 },
//     ],
//     newPostText: 'it-kamasutra.com'
//   },
//   dialogsPage: {
//     messages: [
//       { di: 1, my: false, message: "Hi" },
//       { di: 1, my: true, message: "Zdorova " },
//       { di: 1, my: false, message: "How is your it-kamasutra?" },
//       { di: 1, my: true, message: "Are you stupid?!" },
//     ],
//     dialogs: [
//       { id: 1, online: false, name: "Dimych" , ava: "https://avatars.dzeninfra.ru/get-zen_doc/119173/pub_5c126713379cb200ad4a97e6_5c126c2b1371c600ab5edfcf/scale_1200"},
//       { id: 2, online: true, name: "Andrey" , ava: "https://masterpiecer-images.s3.yandex.net/7300c5d5725411eeabdb6ac6a1596643:upscaled"},
//       { id: 3, online: true, name: "Sveta" , ava: "https://avatars.mds.yandex.net/get-shedevrum/16106905/img_010fdadaf14211ef82c4caf2840a7b5b/orig"},
//       { id: 4, online: false, name: "Sasha" , ava: "https://avatars.mds.yandex.net/get-shedevrum/10254163/img_0c2ff387f10b11ef805132129414c20c/orig"},
//       { id: 5, online: true, name: "Viktoria" , ava: "https://avatars.mds.yandex.net/get-shedevrum/14784426/img_05a06c3fefa411efb7328a1f92f7a718/orig"},
//       { id: 5, online: true, name: "Viktor" , ava: "https://avatars.mds.yandex.net/get-shedevrum/14784426/img_348f4048f12811efa4f986c50544bce9/orig"},
//       { id: 6, online: false, name: "Valera" , ava: "https://avatars.mds.yandex.net/get-shedevrum/15252934/img_a1b0d02eec6411ef95d2561e34a05e01/orig"},
//     ],
//     newMessageText: ''
//   },
// };

// window.state = state


// export let addPost = () => {
//   // debugger;
//   const newPost = {
//     id: 5,
//     message: state.profilePage.newPostText,
//     likesCount: 0
//   }
//   state.profilePage.posts.push(newPost)
//   state.profilePage.newPostText = ''
//   rerenderEntireTree(state)
// }

// export const updateNewPostText = (newText) => {
//   state.profilePage.newPostText = newText
//   rerenderEntireTree(state)
// }

// export const addMessage = () => {
//   const newMessage = {
//     id: 1,
//     my: true,
//     message: state.dialogsPage.newMessageText
//   }
//   state.dialogsPage.messages.push(newMessage)
//   state.dialogsPage.newMessageText = ''
//   rerenderEntireTree(state)
// }

// export const updateNewMessage = (newMessage) => {
//   state.dialogsPage.newMessageText = newMessage
//   rerenderEntireTree(state)
// }

// export const subscribe = (observer) => {
//   rerenderEntireTree = observer  // observer - publisher-subscriber
// }

// export default state;
const store = {
  _state: {
    profilePage: {
      posts: [
        { di: 1, message: "Hi, how are you?", likesCount: 11 },
        { di: 1, message: "It's my first post", likesCount: 12 },
        { di: 1, message: "What is it man?", likesCount: 5 },
        { di: 1, message: "I'm ready up and runing!", likesCount: 100 },
      ],
      _newPostText: 'it-kamasutra.com'
    },
    dialogsPage: {
      messages: [
        { di: 1, my: false, message: "Hi" },
        { di: 1, my: true, message: "Zdorova " },
        { di: 1, my: false, message: "How is your it-kamasutra?" },
        { di: 1, my: true, message: "Are you stupid?!" },
      ],
      dialogs: [
        { id: 1, online: false, name: "Dimych" , ava: "https://avatars.dzeninfra.ru/get-zen_doc/119173/pub_5c126713379cb200ad4a97e6_5c126c2b1371c600ab5edfcf/scale_1200"},
        { id: 2, online: true, name: "Andrey" , ava: "https://masterpiecer-images.s3.yandex.net/7300c5d5725411eeabdb6ac6a1596643:upscaled"},
        { id: 3, online: true, name: "Sveta" , ava: "https://avatars.mds.yandex.net/get-shedevrum/16106905/img_010fdadaf14211ef82c4caf2840a7b5b/orig"},
        { id: 4, online: false, name: "Sasha" , ava: "https://avatars.mds.yandex.net/get-shedevrum/10254163/img_0c2ff387f10b11ef805132129414c20c/orig"},
        { id: 5, online: true, name: "Viktoria" , ava: "https://avatars.mds.yandex.net/get-shedevrum/14784426/img_05a06c3fefa411efb7328a1f92f7a718/orig"},
        { id: 5, online: true, name: "Viktor" , ava: "https://avatars.mds.yandex.net/get-shedevrum/14784426/img_348f4048f12811efa4f986c50544bce9/orig"},
        { id: 6, online: false, name: "Valera" , ava: "https://avatars.mds.yandex.net/get-shedevrum/15252934/img_a1b0d02eec6411ef95d2561e34a05e01/orig"},
      ],
      _newMessageText: ''
    },
  },
  _callSubscriber: () => {
    alert('У меня нет субскрайбера')
  },
  getState() {
    return this._state
  },
  subscribe(observer) {
    this._callSubscriber = observer
  },
  addPost() {

    const newPost = {
      id: 1,
      message: this._state.profilePage._newPostText,
      likesCount: 5
    }
    this._state.profilePage.posts.push(newPost)
    this._state.profilePage._newPostText = ''
    this._callSubscriber(this)
  },
  updateNewPostText(newText) {
    this._state.profilePage._newPostText = newText
    this._callSubscriber(this)
  },
  addMessage() {
    const newMessage = {
      id: 1,
      my: true,
      message: this._state.dialogsPage._newMessageText
    }
    this._state.dialogsPage.messages.push(newMessage)
    this._state.dialogsPage._newMessageText = ''
    this._callSubscriber(this)
  },
  updateNewMessage(newMessage) {
    this._state.dialogsPage._newMessageText = newMessage
    this._callSubscriber(this)
  },
  dispatch(action) {
    // debugger
    if (action.type === 'ADD-POST') {
      const newPost = {
        id: 1,
        message: this._state.profilePage._newPostText,
        likesCount: 5
      }
      this._state.profilePage.posts.push(newPost)
      this._state.profilePage._newPostText = ''
      this._callSubscriber(this)

    } else if (action.type === 'UPDATE-NEW-POST-TEXT') {

      this._state.profilePage._newPostText = action.newText
      this._callSubscriber(this)
    }
  }
}
export default store
window.newState = store