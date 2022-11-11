import Styles from './Home.module.css';

import { IVideo } from '../../interfaces/videos';
import { SearchBar } from '../../components/SearchBar/SearchBar';
import { VideoCard } from '../../components/VideoCard/VideoCard';
import { useGetVideos } from '../../hooks/useGetVideos/useGetVideos';

export const Home = () => {
  const { videos, search } = useGetVideos();

  return (
    <main className={Styles.container}>
      <SearchBar searchCallback={search} />
      <section className={Styles.videos}>
        {videos.map((video, index) => {
          return <VideoCard video={video} key={video.url} />;
        })}
      </section>
    </main>
  );
};
