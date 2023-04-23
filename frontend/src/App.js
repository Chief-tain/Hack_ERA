import { Routes, Route } from 'react-router-dom'
import HomePage from './pages/HomePage';
import CardPage from './pages/CardPage';
import NotFoundPage from './pages/NotFoundPage';
import CardsPage from './pages/CardsPage';

import './../src/assets/css/App.css'
import Layout from './components/Layout';


function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Layout />}>
          <Route index element={<HomePage />} />
          <Route path='cards' element={<CardsPage />} />
          <Route path='cards/:id_data' element={<CardPage />} />
          <Route path='*' element={<NotFoundPage />} />
        </Route>
      </Routes>
    </>
  );
}

export default App;
