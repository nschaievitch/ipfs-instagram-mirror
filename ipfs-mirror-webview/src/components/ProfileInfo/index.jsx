const ProfileInfo = ({ profileInfo, getUrlFromProfileFile }) => {
  return (
    <div className="w-75 mx-auto">
      <img
        src={getUrlFromProfileFile(`/media/${profileInfo.profilePic}`)}
        alt={profileInfo.username}
        className="profilePicLarge mb-2"
      />
      <h2>{profileInfo.username}</h2>
      <h5 className="text-secondary">{profileInfo.name}</h5>
      <p>{profileInfo.bio}</p>
    </div>
  );
};

export default ProfileInfo;
