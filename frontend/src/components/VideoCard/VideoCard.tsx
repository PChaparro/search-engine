import Styles from './VideoCard.module.css';
import { IVideo } from '../../interfaces/videos';

interface IProps {
  video: IVideo;
}

export const VideoCard = ({ video }: IProps) => {
  return (
    <article className={Styles.card}>
      <a href={video.url} target='_blank' rel='noopener'>
        <img src={video.thumbnail} alt={video.title} className={Styles.card__image} />
      </a>
      <div className={Styles.card__body}>
        <a href={video.url} target='_blank' rel='noopener'>
          <h3 className={Styles.card__title}>{video.title}</h3>
        </a>
        <div className={Styles.card__tags}>
          {video.tags.length !== 0 &&
            video.tags.slice(0, 3).map((tag: string, index: number) => {
              return (
                <span className={Styles.card__tag} key={`${video.url}-${index}`}>
                  {tag}
                </span>
              );
            })}
        </div>
      </div>
    </article>
  );
};
