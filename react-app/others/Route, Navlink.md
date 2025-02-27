__                                                         __Routing__
> npm react-router-dom
> import { BrowserRouter, Routes, Route, Navlink } from 'react-router-dom'

<BrowserRouter>
	<Routes>
		<Route path="/profile" element={<Profile />} />
		<Route path="/dialogs/*" element={<Dialogs />} />
		// если необходимо задать урл для доерних урлов
	</Routes>
</BrowserRouter>

```jsx
<NavLink className={({isActive}) => isActive ? `${s.active} ${s.class1}` : s.class1} to="/profile" > Profile </NavLink>

<NavLink to="/dialogs/1"> Dimych </Navlink>

```
