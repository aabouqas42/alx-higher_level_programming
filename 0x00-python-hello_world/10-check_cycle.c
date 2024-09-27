#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t	*slow;
	listint_t	*fast;

	slow = list;
	fast = slow;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return 1;
	}
	return 0;
}
