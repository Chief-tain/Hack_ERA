import { NavLink } from 'react-router-dom'

import Logo from '../assets/image/dron_navbar.svg'
import '../assets/css/Navbar.css'

const Navbar = () => {
  return (
    <header className='navbar'>
      <img src={Logo} alt="icon" />
      <div className='title'>Комплектующие для БПЛА</div>
      <div className='nav'>
        <NavLink to='/' className='nav-link'>Главная</NavLink>
        <NavLink to='/cards' className='nav-link'>Окно после поиска</NavLink>
        <NavLink to='/cards/1' className='nav-link'>Окно карточки</NavLink>
      </div>
    </header>
  )
}

export default Navbar