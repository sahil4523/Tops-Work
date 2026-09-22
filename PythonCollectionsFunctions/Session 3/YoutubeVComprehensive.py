def video_views(titles, views):
    return [(title, round(view, -3))
            for title, view in zip(titles, views)]

titles=["Python Tutorial", "C Tutorial", "Java Tutorial"]
views=[12500, 8300, 25600]

result=video_views(titles, views)

print(result)