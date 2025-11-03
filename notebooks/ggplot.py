import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell
def _():
    import numpy as np
    import polars as pl

    from nullmodels import geom_pr_hypergeom
    from plotnine import ggplot, aes, geom_point, ggtitle, theme_bw
    return (
        aes,
        geom_point,
        geom_pr_hypergeom,
        ggplot,
        ggtitle,
        np,
        pl,
        theme_bw,
    )


@app.cell
def _(aes, geom_point, geom_pr_hypergeom, ggplot, ggtitle, np, pl, theme_bw):
    random_noise = pl.DataFrame(
        np.random.uniform(0.5, 1, (10, 2)), schema=["precision", "recall"]
    )

    (
        ggplot(random_noise)
        + aes("recall", "precision")
        + geom_point()
        + geom_pr_hypergeom(200, method="tail", h0_correct=0.3)
        + ggtitle("30% correct tail case nullmodel $q_{0.9}$")
        + theme_bw()
    ).show()
    return


if __name__ == "__main__":
    app.run()
