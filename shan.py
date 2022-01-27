class ThemeCodeActivity : BaseActivity<ThemeCodeMvp.View, ThemeCodePresenter>(), ThemeCodeMvp.View {
 
    val spinner: AppCompatSpinner by bindView(R.id.themesList)
    val webView: PrettifyWebView by bindView(R.id.webView)
    val progress: ProgressBar? by bindView(R.id.readmeLoader)
 
    override fun layout(): Int = R.layout.theme_code_layout
 
    override fun isTransparent(): Boolean = false
 
    override fun canBack(): Boolean = true
 
    override fun isSecured(): Boolean = false
 
    override fun providePresenter(): ThemeCodePresenter = ThemeCodePresenter()
 
    @OnClick(R.id.done) fun onSaveTheme() {
        val theme = spinner.selectedItem as String
        PrefGetter.setCodeTheme(theme)
        setResult(Activity.RESULT_OK)
        finish()
    }
 
    override fun onInitAdapter(list: List<String>) {
        spinner.adapter = ArrayAdapter<String>(this, android.R.layout.simple_spinner_dropdown_item, list)
    }
 
    @OnItemSelected(R.id.themesList) fun onItemSelect() {
        val theme = spinner.selectedItem as String
        webView.setThemeSource(CodeThemesHelper.CODE_EXAMPLE, theme)
    }
 
 
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        progress?.visibility = View.VISIBLE
        webView.setOnContentChangedListener(this)
        title = ""
        presenter.onLoadThemes()
    }
 
    override fun onContentChanged(p: Int) {
        progress?.let {
            it.progress = p
            if (p == 100) it.visibility = View.GONE
        }
    }
 
    override fun onScrollChanged(reachedTop: Boolean, scroll: Int) {}
}
