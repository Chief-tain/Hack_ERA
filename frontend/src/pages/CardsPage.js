import { useState, useEffect } from "react"
import axios from 'axios'
import { Link } from "react-router-dom"

import '../assets/css/CardsPage.css'

const CardsPage = () => {
  const [cards, setCards] = useState([])

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/get_data?page=1&size=50')
      .then(res => {
        console.log(res.data.items)
        setCards(res.data.items)
      })
      .catch(err => {
        console.log(err);
      })
  }, [])

  return (
    <>
      <div className='grid'>
        {
          cards.map(card => (
            <div className="card">
              <Link key={card.id_data} to={`/cards/${card.id_data}`} className='card'>
                <div className='name element'>
                  {card.name}
                </div>
                <div className='url element'>
                  {card.url}
                </div>
                <div className='price element'>
                  {card.price}
                </div>
              </Link>
            </div>
          ))
        }
      </div>
    </>
  )
}

export default CardsPage