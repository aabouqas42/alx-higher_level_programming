#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t	*head;

	head = list;
	while (list->next)
	{
		if (head == list->next)
			return 1;
		if (list->next && head == list->next)
			return 1;
		if (list->next && list->next->next && head == list->next->next)
			return 1;
		if (list->next && list->next->next && list->next->next->next && head == list->next->next->next)
			return 1;
		if (list->next && list->next->next && list->next->next->next && list->next->next->next->next && head == list->next->next->next->next)
			return 1;
		if (list->next && list->next->next && list->next->next->next && list->next->next->next->next)
			list = list->next->next->next->next;
		else if (list->next && list->next->next && list->next->next->next)
			list = list->next->next->next;
		else if (list->next && list->next->next)
			list = list->next->next;
		else
			list = list->next;
	}
	return 0;
}
