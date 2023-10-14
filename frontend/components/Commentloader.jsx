import { useState } from "react"



export default function CommentsPage() {

    const [comments, setComments] = useState([])

    const fetchComments = async () => {
        const response = await fetch('api/comments')
        const data = await response.json()
        setComments(data)
    }
    return (
        <>
        <button className="bg-slate-200 p-1 border rounded border-gray-800 hover:bg-slate-500" onClick={fetchComments}>Find Peak</button>
        {
            comments.map(comment => {
                return (
                    <div key={comment.id}>
                    {comment.id} {comment.text}
                    </div>
                )
            })
        }
        </>
    )
}
