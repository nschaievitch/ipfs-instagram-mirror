import React, { useState, useEffect } from 'react'
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"
import Post from "./components/Post"
import ProfileInfo from './components/ProfileInfo'

function App() {

  const [gateway, setGateway] = useState("https://gateway.ipfs.io")
  const [profile, setProfile] = useState("")
  const [profileInfo, setProfileInfo] = useState("")

  const fetchJSONData = async (url) => {
    const res = await fetch(url)
    const json = await res.json()

    return json
  }

  const getUrlFromProfileFile = (filePath) => {
    return `${gateway}${profile}${filePath}`
  }

  useEffect(() => {
    if (profile !== "") {
      fetchJSONData(getUrlFromProfileFile("/info.json")).then(setProfileInfo)
    }

    
  }, [profile, gateway])

  return (
    <div className="container">
      <div className="w-75 mx-auto my-5"><Form.Control placeholder="Profile address" value={profile} onChange={(e) => setProfile(e.target.value)}/></div>
      {profileInfo && <ProfileInfo profileInfo={profileInfo} getUrlFromProfileFile={getUrlFromProfileFile}/>}
      {profileInfo && profileInfo.posts.map((post) => <Post post={post} getUrlFromProfileFile={getUrlFromProfileFile} profileInfo={profileInfo}/>)}
    </div>
  )
}

export default App
