import { useParams } from 'react-router-dom'
import { useState, useEffect } from 'react'
import axios from 'axios'

const CardPage = () => {
  const { id_data } = useParams()
  const [card, setCard] = useState(null)

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/api/get_item?id=${id_data}`)
      .then(res => {
        console.log(res.data.items)
        setCard(res.data.items)
      })
      .catch(err => {
        console.log(err);
      })
  }, [id_data])

  return (
    <>
      {id_data}
    </>
  )
}

/*
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
*/

export default CardPage
