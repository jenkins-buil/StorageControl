import blogFetch from "../axios/config"
import { useState, useEffect } from "react"
import { Link } from "react-router-dom"

const Categoria = () => {
    const [getAll, setGetAll] = useState()

    const getCategorias = async() => {
        try {
            const response = await blogFetch.get('/categorias')
            const data = response.data
            setGetAll(data)
        } catch (error) {
            console.log(error)
        }
    }
    
    useEffect(() => {
        getCategorias()
    }, [])

  return (
    <div className='home'>
      <h1>Categorias</h1>
      {!getAll ? (<p>Carregando....</p>) : (
        getAll.map((post) => (
          <div className="post" key={post.id}>
            <p><strong>Categoria: </strong>{post.categoria}</p>
            <p><strong>id: </strong>{post.id}</p>
            <Link to={`/new/${post.id}`} className='btn'>
              Continuar
            </Link>
          </div>
        ))
      )}
    </div>
  )
}

export default Categoria