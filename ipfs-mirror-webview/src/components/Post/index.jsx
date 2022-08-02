import Carousel from "react-bootstrap/Carousel";

const Post = ({ post, getUrlFromProfileFile, profileInfo }) => {
  return (
    <div className="w-75 mx-auto my-5 border p-3">
        <div className="d-flex mb-2 align-items-center">
            <img className="profilePicSmall" src={getUrlFromProfileFile(`/media/${profileInfo.profilePic}`)} />
            <strong className="m-2">{profileInfo.username}</strong>
        </div>
      <Carousel interval={null} className="mb-3">
        {post.imgs.map((img) => {
          return (
            <Carousel.Item>
              <img
                className="d-block w-100"
                src={getUrlFromProfileFile(`/media/${img}`)}
              />
            </Carousel.Item>
          );
        })}
      </Carousel>
      <span><strong>{profileInfo.username} </strong>{post.caption}</span> <br />
      <span className="text-secondary">{post.timestamp}</span>
    </div>
  );
};

export default Post;
