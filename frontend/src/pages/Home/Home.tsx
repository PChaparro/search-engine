import Styles from './Home.module.css';

import { BallTriangle } from '@agney/react-loading';
import { SearchBar } from '../../components/SearchBar/SearchBar';
import { VideoCard } from '../../components/VideoCard/VideoCard';
import { useGetVideos } from '../../hooks/useGetVideos/useGetVideos';

export const Home = () => {
  const { videos, search, isLoading } = useGetVideos();

  return (
    <main className={Styles.container}>
      <SearchBar searchCallback={search} />
      {isLoading && <div className={Styles.loader}><BallTriangle color='#4766da' width={72} /></div>}
      <section className={Styles.videos}>
        {!isLoading &&
          videos.map((video, index) => {
            return <VideoCard video={video} key={video.url} />;
          })}
      </section>
    </main>
  );
};
