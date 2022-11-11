import Styles from './SearchBar.module.css';

export const SearchBar = () => {
  return (
    <header className={Styles.header}>
      <h1 className={Styles.header__title}>Search engine</h1>
      <form className={Styles.header__form}>
        <div className={Styles.header__group}>
          <label htmlFor='criteria' hidden>
            Search criteria
          </label>
          <div className={Styles.header__wraper}>
            <input
              type='text'
              id='criteria'
              name='criteria'
              placeholder='Your search here'
              className={Styles.header__input}
            />
            <input type='submit' value='search' className={Styles.header__submit} />
          </div>
        </div>
      </form>
    </header>
  );
};
