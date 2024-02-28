import blogFetch from "../axios/config"
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import "./Post.css"
import { Link } from "react-router-dom"
const Post = () => {
  
  const { id } = useParams()

  const [posts, setPosts] = useState({})

  const getPost = async() => {
    try {
      const response = await blogFetch.get(`/produtos/${id}`)
      const data = response.data
      console.log( await data[0].categoria_id)
      
      
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    getPost()
  }, [])
  
  return (
    <div className="post-container">
      {!posts[0] ? (
        <p>Carregando...</p>
      ) : ( 
      <div className="post">
        <p><strong>Marca: </strong>{posts[0].marca}</p>
        <p><strong>Tamanho: </strong>{posts[0].tamanho}</p>
        <p><strong>Quantidade: </strong>{posts[0].quantidade}</p>
      </div>
      )}
      <div className="container-excluir"><Link className="btn-details">Excluir</Link></div>
      <div className="container-editar"><Link className="btn-details">Editar</Link></div>
    </div>
  )
}

export default Post