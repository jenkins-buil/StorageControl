import blogFetch from '../axios/config'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useParams } from 'react-router-dom'

import "./NewPost.css"
const NewPost = () => {

  const { id } = useParams()

  const navigate = useNavigate()

  const [marca, setMarca] = useState()
  const [tamanho, setTamanho] = useState()
  const [cor, setCor] = useState()
  const categoria_id = id

  const createPost = async(e) => {
    e.preventDefault()
    
    await blogFetch.post("/produtos", {
      marca,
      tamanho,
      cor,
      categoria_id
    })
    navigate("/")
  }

  return (
    <div className='new-post'>
      <h2>Inserir produto: </h2>
      <form onSubmit={(e) => createPost(e)}>
      <div className="form-control">
        <label htmlFor="marca-produto">Marca Produto</label>
        <input 
          type="text" 
          name='marca-produto' 
          id='marca-produto' 
          placeholder='Marca do produto'
          onChange={(e) => setMarca(e.target.value)}
        />
      </div>
      <div className="form-control">
        <label htmlFor="tamanho-produto">Tamanho Produto</label>
        <input 
          type="text" 
          name='tamanho-produto' 
          id='tamanho-produto' 
          placeholder='Tamanho do produto'
          onChange={(e) => setTamanho(e.target.value)}
        />
      </div>
      <div className="form-control">
        <label htmlFor="cor-produto">Cor Produto</label>
        <input 
          type="text" 
          name='cor-produto' 
          id='cor-produto' 
          placeholder='Cor do produto'
          onChange={(e) => setCor(e.target.value)}
        />
      </div>
      <input type="submit" value="Cadastrar" className='btn'/>
      </form>
    </div>
  )
}

export default NewPost