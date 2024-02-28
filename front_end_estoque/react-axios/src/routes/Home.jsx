import blogFetch from "../axios/config"
import { useState, useEffect } from "react"
import { Link } from "react-router-dom"
import "./Home.css"


const Home = () => {

  const [posts, setPost] = useState([])

  const getPosts = async() => {
    try {
      const response = await blogFetch.get("/produtos")
      const data = response.data
      setPost(data)
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    getPosts()
  }, [])
  
  return (
    <div className='home'>
      <h1>Produtos em estoque</h1>
      {posts.length === 0 ? (<p>Carregando....</p>) : (
        posts.map((post) => (
          <div className="post" key={post.id}>
            <p><strong>Marca: </strong>{post.marca}</p>
            <p><strong>Tamanho: </strong>{post.tamanho}</p>
            <p><strong>Cor: </strong>{post.cor}</p>
            <p><strong>Quantidade: </strong>{post.quantidade}</p>
            <Link to={`/produtos/${post.id}`} className='btn'>
              Produto
            </Link>
          </div>
        ))
      )}
    </div>
  )
}

export default Home