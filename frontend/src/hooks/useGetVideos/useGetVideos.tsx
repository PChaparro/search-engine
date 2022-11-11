import { useState } from 'react';
import { IVideo } from '../../interfaces/videos';
import { SearchVideosService } from '../../services/videos.services';

export const useGetVideos = () => {
  const [videos, setVideos] = useState(Array<IVideo>);

  const search = async (criteria: string) => {
    const videos = await SearchVideosService(criteria);
    setVideos(videos);
  };

  return {
    videos,
    search,
  };
};
